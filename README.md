# YouTube Fishing Videos Data Analysis

This project ingests YouTube video data (specifically fishing-related videos) using the YouTube Data API, stores the data in MongoDB, and provides a dashboard for visualizing the video data using Metabase.

## Project Structure
The project includes the following components:
1. **Data Ingestion Service**: A Python service that uses the YouTube Data API to fetch fishing-related videos and their metadata, storing the data in MongoDB.
2. **MongoDB**: NoSQL database to store YouTube video data and metadata.
3. **Metabase**: Business intelligence (BI) tool to visualize and explore the stored data.
4. **Docker Compose**: Orchestrates MongoDB, Metabase, and the data ingestion service within a unified network.
   
## Requirements
- [YouTube Data API v3 key](https://developers.google.com/youtube/v3/getting-started)
- [Docker](https://docs.docker.com/get-started/)

## Setup
1. Clone the Repo
    ```
    git clone https://github.com/lopezj1/youtube_fishing.git
    cd youtube_fishing
    ```
2. Create `.env` file 
   Add the following variables to the `.env` file in the project directory:
    ```
    YOUTUBE_API_KEY=your_youtube_api_key
    MONGO_INITDB_ROOT_USERNAME=root
    MONGO_INITDB_ROOT_PASSWORD=password
    MONGO_DB_NAME=youtube_data
    ```
3. Start the Services
   Run `docker-compose up -d` to start all services using Docker Compose:
   - MongoDB: 
     - Connect using the connection string: `mongodb://root:password@0.0.0.0:27017/`
     - Use MongoDB tools or extensions like the MongoDB VSCode plugin
   - Metabase:
     - Access at http://localhost:3000
     - Default credentials:
       - Username: admin
       - Password: admin
   - Data Ingestion Service:
     - Automatically runs the ingestion script upon container start.

## Dashboard
Once the data is ingested, explore it through the Metabase dashboard. Below is a sample visualization:

![Dashboard](./img/dashboard.png)

## Future Considerations
- Add more filters and visualizations to the dashboard.
- Add pagination to the data ingestion to handle multi-page results.
- Implement error handling on data ingestion.