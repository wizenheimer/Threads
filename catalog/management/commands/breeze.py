import pandas as pd
from django.core.management.base import BaseCommand
from pathlib import Path
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

        cleaned_csv_path = self.clean_up(path=absolute_path)
        self.stdout.write(self.style.SUCCESS("Data cleaned up. Preparing to load..."))

        # TODO: switch to vectorized solution
        if wipe:
            SubCategory.objects.all().delete()
            Category.objects.all().delete()
            Product.objects.all().delete()

        df = pd.read_csv(cleaned_csv_path)

        category = df["Category"].to_numpy()
        sub_category = df["Sub Category"].to_numpy()
        product_type = df["Product Type"].to_numpy()
        alt_type = df["Alt Type"].to_numpy()
        brand = df["Brand Name"].to_numpy()
        title = df["Name"].to_numpy()
        product_url = df["URL"].to_numpy()

        for cat, sub_cat, prod_type, alt, brand_name, prod_title, url in zip(
            category, sub_category, product_type, alt_type, brand, title, product_url
        ):
            category = Category.objects.get_or_create(
                title=cat,
            )[0]
            sub_category = SubCategory.objects.get_or_create(
                title=sub_cat,
                category=category,
            )[0]
            product = Product.objects.get_or_create(
                brand=brand_name,
                product_type=prod_type,
                alt_type=alt,
                product_url=url,
                title=prod_title,
                sub_category=sub_category,
            )

        self.stdout.write(self.style.SUCCESS(f"Loaded csv into the model"))
        self.stdout.write(self.style.SUCCESS(f"Cleaning up.."))
        cleaned_csv_path.unlink()
        self.stdout.write(self.style.SUCCESS(f"Done."))
