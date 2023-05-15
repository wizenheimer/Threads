# Threads 📦

Backend Component for DSN3099 Project

- Scraped and cleaned over 766 products using Lambda + S3
- Performed zero-shot product classification using LLM
- Keyword Search : ElasticSearch
- Semantic Search : Bert Embeddings + FAISS
- Created Endpoints for fetching data and performing queries

## 🥡 System Design

![image](https://github.com/wizenheimer/Threads/assets/91504165/a1f54032-f8bd-4f8c-92e1-e264b8e602b6)
For the List View we could run queries against the keywords endpoint

![image](https://github.com/wizenheimer/Threads/assets/91504165/4178fb67-0246-4555-836c-4936c4e5693e)
For the Detail View we could run queries against the semantic endpoint

![image](https://github.com/wizenheimer/Threads/assets/91504165/2b745a25-9df2-4c49-842f-03018346d607)
Scrapper Overview

## 📌 Enhancements
![0_oyD7ekV-hMU91h4J](https://github.com/wizenheimer/Threads/assets/91504165/962d3af9-d81d-44a0-850a-d99e13c08568)

Since the project was wrapped up within 24 hours, here are a few enhancements which I would like to pick up (P.S. my professor asked me to do this 🤖)
- Cache Endpoints using Redis [ETA: 3hrs]
- Explore Semantic Cache [ETA: 4.5hrs]
- Use Distributed Task Queue for long running blocking tasks [ETA: 3hrs]
- Use Distributed Queues to tackle link rots [ETA: 3hrs]

## 🪦 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
        
## 🍰 Contributing    
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Before contributing, please read the [code of conduct](CODE_OF_CONDUCT.md) & [contributing guidelines](CONTRIBUTING.md).
       
