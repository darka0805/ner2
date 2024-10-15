import pandas as pd
"""
I decided to use dataset that already exists in kaggle, here is the <a href="[your_url_here](https://www.kaggle.com/datasets/geraygench/mountain-ner-dataset/data)">link</a>. Each entry in the dataset corresponds to a tweet or a sentence that was generated by OpenAI's ChatGPT. It's a mixed dataset that includes a variety of tweets/texts, some of which are focused on mountain-related experiences, while others may discuss different topics.


This dataset consists of two columns
- text
    - This feature contains the actual text content of each sentence/tweet. It captures the expressions, experiences, or sentiments related to mountainous regions and activities
- marker
    - In the context of the provided code, the "marker" feature represents the start and end indices of the occurrences of specific mountain names within the tweet text
"""
df_path = "/content/sample_data/mountain_dataset_with_markup.csv"

df = pd.read_csv(df_path, encoding='utf-8')
df.head()