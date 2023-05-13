import pandas as pd
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from pathlib import Path
import csv
from catalog.models import Product, Category, SubCategory


class Command(BaseCommand):
    help = "Populate Database using CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            "-p",
            type=str,
            help="Indicates the relative path of the CSV file",
        )
        parser.add_argument(
            "--offset",
            "-o",
            type=int,
            help="Indicates the offset",
        )
        parser.add_argument(
            "--wipe",
            "-w",
            type=bool,
            help="Indicates whether to wipe the database prior to loading",
        )

    def clean_up(self, path):
        df = pd.read_csv(path)
        self.stdout.write(self.style.SUCCESS("Preparing to clean data.."))
        df.dropna()
        cleaned_csv_path = path.parent / f"{path.stem}_cleaned.csv"
        df.to_csv(cleaned_csv_path)
        return cleaned_csv_path

    def handle(self, *args, **kwargs):
        path = Path(kwargs.get("path", None))
        offset = kwargs.get("offset", 1)
        wipe = kwargs.get("wipe", True)

        if path is None:
            self.stdout.write(self.style.ERROR("Path not specified."))
            return

        if not path.exists():
            self.stdout.write(self.style.ERROR("Path does not exist."))

        absolute_path = path.resolve()
        self.stdout.write(
            self.style.SUCCESS("Path discovered.. performing data sanitization.,.")
        )

        cleaned_csv = self.clean_up(path=absolute_path)
        self.stdout.write(self.style.SUCCESS("Data cleaned up. Preparing to load..."))

        count = 0
        # TODO: switch to vectorized solution
        with open(cleaned_csv, encoding="utf8") as file:
            reader = csv.reader(file)
            for _ in range(0, offset):
                next(reader)  # Advance past the header

            if wipe:
                SubCategory.objects.all().delete()
                Category.objects.all().delete()
                Product.objects.all().delete()

            for row in reader:
                count += 1
                category = Category.objects.get_or_create(
                    title=row[0],
                )[0]
                sub_category = SubCategory.objects.get_or_create(
                    title=row[1],
                    category=category,
                )[0]
                product = Product.objects.get_or_create(
                    brand=row[2],
                    product_type=row[3],
                    alt_type=row[4],
                    product_url=row[5],
                    title=row[6],
                    sub_category=sub_category,
                )
        self.stdout.write(self.style.SUCCESS(f"Loaded {count} into the model"))
