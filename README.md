# AI-Driven-Fashion-Recommendation-System-for-Personalized-Shopping-Experiences

## Introduction

This report details the development of a hyper-personalized fashion recommendation system using a dataset collected from Kaggle. The dataset contains product information from a fashion store, including product IDs, names, brands, gender specifications, prices, number of images, descriptions, and primary colors. The recommendation system is built using state-of-the-art machine learning techniques, including Large Language Models (LLMs), chunking, sentence transformers, FAISS (Facebook AI Similarity Search), GPT-3.5 turbo, and Streamlit.

<img width="1433" alt="Screenshot 2024-07-11 at 7 40 01 PM" src="https://github.com/user-attachments/assets/b90b9c96-d379-4189-87a0-912463e090e1">


## Dataset Overview

The dataset used for this project was collected from Kaggle and contains the following columns:

- **ProductID**: The unique identifier for each product.
- **ProductName**: The name of the product.
- **ProductBrand**: The brand of the product.
- **Gender**: The gender for which the product is intended.
- **Price (INR)**: The price of the product in Indian Rupees.
- **NumImages**: The number of images available for the product.
- **Description**: A textual description of the product.
- **PrimaryColor**: The primary color of the product.

## Project Goals

The primary goal of this project is to develop a recommendation system that can provide highly personalized fashion recommendations to users based on their preferences and search history. The system aims to enhance the shopping experience by offering relevant and customized product suggestions.

## Methodology

### Data Preprocessing

1. **Data Cleaning**: Remove any null or duplicate entries from the dataset.
2. **Text Preprocessing**: Clean and preprocess textual data in the description column using techniques such as tokenization, stemming, and lemmatization.

### Model Building

1. **Chunking**: Split long product descriptions into manageable chunks for better processing and understanding.
2. **Sentence Transformer**: Use a sentence transformer to convert product descriptions into embeddings, capturing semantic meaning.
3. **FAISS**: Implement FAISS for efficient similarity search and retrieval of relevant products.
4. **GPT-3.5 Turbo**: Utilize GPT-3.5 turbo to generate personalized recommendations based on user queries and preferences.
5. **Streamlit**: Develop an interactive user interface using Streamlit to display recommendations and allow users to interact with the system.

### Recommendation System Workflow

1. **User Query**: The user inputs a query or selects preferences.
2. **Embedding Generation**: Convert the query and product descriptions into embeddings using the sentence transformer.
3. **Similarity Search**: Use FAISS to find the most similar products based on the embeddings.
4. **Recommendation Generation**: GPT-3.5 turbo generates personalized recommendations by considering the user query and the retrieved similar products.
5. **Display Results**: Present the recommended products to the user through the Streamlit interface.

## Benefits to the Organization

- **Enhanced User Experience**: Providing personalized recommendations improves the shopping experience and increases user satisfaction.
- **Increased Engagement**: Tailored product suggestions keep users engaged and encourage them to explore more products.
- **Improved Sales**: Relevant recommendations can lead to higher conversion rates and increased sales.
- **Data-Driven Insights**: The system provides valuable insights into user preferences and market trends.


## Conclusion

The hyper-personalized fashion recommendation system leverages advanced AI technologies to provide users with customized shopping experiences. By utilizing LLMs, chunking, sentence transformers, FAISS, GPT-3.5 turbo, and Streamlit, the system can effectively analyze user preferences and deliver relevant product suggestions. Future developments, including the implementation of a knowledge graph and measures to tackle hallucination, will further enhance the system's accuracy and reliability. This project demonstrates the potential of AI in transforming the retail industry by offering innovative and personalized solutions.
