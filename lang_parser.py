import os

from dotenv import load_dotenv, find_dotenv


import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv(find_dotenv())
google_api_key = os.getenv("GOOGLE_API_KEY")


def get_completion(prompt, model="gemini-2.0-pro-exp"):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-pro-exp",
    temperature=0.7,
    google_api_key=google_api_key
)
    response = llm.invoke(prompt)
    return response.content

email_response = """
Here's our itinerary for our upcoming trip to Europe.
We leave from Denver, Colorado airport at 8:45 pm, and arrive in Amsterdam 10 hours later
at Schipol Airport.
We'll grab a ride to our airbnb and maybe stop somewhere for breakfast before 
taking a nap.

Some sightseeing will follow for a couple of hours. 
We will then go shop for gifts 
to bring back to our children and friends.  

The next morning, at 7:45am we'll drive to to Belgium, Brussels - it should only take aroud 3 hours.
While in Brussels we want to explore the city to its fullest - no rock left unturned!

"""

email_template = f"""
From the following email, extract the following information:

leave_time: when are they leaving for vacation to Europe. If there's an actual
time written, use it, if not write unknown.

leave_from: where are they leaving from, the airport or city name and state if
available.

cities_to_visit: extract the cities they are going to visit. 
If there are more than one, put them in square brackets like '["cityone", "citytwo"].

Format the output as JSON with the following keys:
leave_time
leave_from
cities_to_visit

email: {email_response}
"""


# print(type(get_completion(prompt=email_template)))


#==== Langchain Parsers ====
from langchain.output_parsers import ResponseSchema as rs
from langchain.output_parsers import StructuredOutputParser as sop


leave_time_schema = rs(name="leave_time",
                                   description="When they are leaving. \
                                       It's usually a numberical time of the day. \
                                           If not available wirte n/a")
leave_from_schema = rs(name="leave_from",
                                      description="Where are they leaving from.\
                                          it's a city, airport or state, or province")
cities_to_visit_schema = rs(name="cities_to_visit",
                                    description="The cities, towns they will be visiting on \
                                        their trip. This needs to be in a list")




response_schema = [
    leave_time_schema,
    leave_from_schema,
    cities_to_visit_schema
]



outup_parser = sop.from_response_schemas(response_schemas=response_schema)

format_instruction = outup_parser.get_format_instructions()

# print(format_instruction)



email_template_revised = f"""
From the following email, extract the following information:

leave_time: when are they leaving for vacation to Europe. If there's an actual
time written, use it, if not write unknown.

leave_from: where are they leaving from, the airport or city name and state if
available.

cities_to_visit: extract the cities they are going to visit. If there are more than 
one, put them in square brackets like '["cityone", "citytwo"].

Format the output as JSON with the following keys:
leave_time
leave_from
cities_to_visit

email: {email_response}
{format_instruction}
"""




response = get_completion(prompt=email_template_revised)

output_dict = outup_parser.parse(response)

print(type(output_dict))


print(output_dict)

print(response)