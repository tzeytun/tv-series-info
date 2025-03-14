# TV Series Info

This project provides information about TV series, including their name, plot, number of seasons, number of episodes, language, and the top 5 main actors. The information is fetched using OpenAI's API.

## Requirements

- Python 3.x
- `openai` library
- `python-dotenv` library

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/tzeytun/tv-series-info.git
   cd tv-series-info
   ```

2. Create a `.env` file in the root directory and add the following environment variables:
   ```
   OPENROUTER_API_KEY=your_openai_api_key
   BASE_URL=your_openai_base_url
   MODEL=your_openai_model
   ```

3. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with the name of the TV series you want to get information about:
```sh
python3 main.py "The Sopranos"
```

## Example Output

Running the script with the series name "The Sopranos" will produce the following output:

```
Name: The Sopranos  
============================  
Plot: The series revolves around Tony Soprano, a New Jersey-based Italian-American mobster, who struggles to balance his family life with his role as the leader of a criminal organization. As he deals with personal and professional challenges, he sees a therapist to manage his anxiety and depression.  
============================  
Genres: Crime, Drama  
============================  
Number of Seasons: 6  
============================
Number of Episodes: 86
============================
IMDB Rating: 9.2/10
============================
Metacritic Score: 92/100
============================
Language: English
============================
Top 5 Main Actors:
1. James Gandolfini (as Tony Soprano)
2. Lorraine Bracco (as Dr. Jennifer Melfi)
3. Edie Falco (as Carmela Soprano)
4. Michael Imperioli (as Christopher Moltisanti)
5. Steven Van Zandt (as Silvio Dante)
============================
```