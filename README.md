# Disease-Symptom-Pred-LLM

 1. Data Collection and Preprocessing:
 ○ Usedrequestsand json to fetch symptom and disease data from external
 APIs.
 ○ UsedpandasandCSVLoader to load and preprocess this data, ensuring it's
 clean and structured.
 2. Generating Embeddings:
 ○ UsedOpenAIEmbeddings to convert symptoms and disease descriptions into
 dense vector representations using the GPT-3.5-turbo model.
 3. Storing and Searching Vectors:
 ○ UsedFAISStostore these embeddings in a vector database, enabling efficient
 similarity searches to match symptoms with potential diseases.
 4. Building the API:
 ○ UsedFastAPI to build an API for your project, with endpoints for predicting
 diseases based on symptoms.
 ○ Handled errors and exceptions using HTTPException.
 5. Interacting with AWS:
 ○ Usedboto3tostore or retrieve data from AWS services, possibly for backup or
 large-scale data processing.
 6. Other Utilities:
 ○ Useditertools.chain to process data in a streamlined manner.
 ○ Usedstrip_markdown to clean up text data.
 ○ Usedosfor environment configuration.
 ○ Usedtimefor performance measurement.
 This setup would allow you to efficiently process and analyze symptom data, generate
 predictions, and serve these predictions through an API

 ● DataManagement: AWS S3 helps manage large datasets efficiently, providing
 scalability and ease of access.
 ● Flexibility: The code handles various file formats and data types by checking and
 converting data as needed.
 ● Resilience: The use of local caching and fallback mechanisms ensures that the
 application remains functional even if there are issues with accessing S3.
 Overall, AWS S3 is used here for its reliable storage and retrieval capabilities, making it a
 suitable choice for managing large and dynamic datasets in your application
