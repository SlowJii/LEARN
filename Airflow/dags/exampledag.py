"""
Example Astronaut ETL DAG (TaskFlow version only)

This DAG queries the list of astronauts currently in space from the
Open Notify API and prints each astronaut’s name and flying craft.

Now written **entirely using TaskFlow API** without any PythonOperator
or context-manager DAG definition.
"""

import requests
from pendulum import datetime
from airflow.decorators import dag, task
from airflow.assets import Asset

# ---------------------------------------------
#   TaskFlow DAG – clean, Pythonic, modern
# ---------------------------------------------
@dag(
    dag_id="example_astronauts_taskflow",
    start_date=datetime(2025, 4, 22),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
    doc_md=__doc__,
)
def example_astronauts_taskflow():

    # -----------------------------
    # Task 1 – Get Astronaut Data
    # -----------------------------
    @task(outlets=[Asset("current_astronauts")])
    def get_astronauts() -> list[dict]:
        """
        Fetch list of astronauts currently in space.
        If the API fails, fallback to hardcoded data.
        """
        try:
            r = requests.get("http://api.open-notify.org/astros.json")
            r.raise_for_status()

            number_of_people_in_space = r.json()["number"]
            list_of_people_in_space = r.json()["people"]

        except Exception:
            print("API unavailable → using fallback data.")
            number_of_people_in_space = 12
            list_of_people_in_space = [
                {"craft": "ISS", "name": "Oleg Kononenko"},
                {"craft": "ISS", "name": "Nikolai Chub"},
                {"craft": "ISS", "name": "Tracy Caldwell Dyson"},
                {"craft": "ISS", "name": "Matthew Dominick"},
                {"craft": "ISS", "name": "Michael Barratt"},
                {"craft": "ISS", "name": "Jeanette Epps"},
                {"craft": "ISS", "name": "Alexander Grebenkin"},
                {"craft": "ISS", "name": "Butch Wilmore"},
                {"craft": "ISS", "name": "Sunita Williams"},
                {"craft": "Tiangong", "name": "Li Guangsu"},
                {"craft": "Tiangong", "name": "Li Cong"},
                {"craft": "Tiangong", "name": "Ye Guangfu"},
            ]

        # Push extra metadata to XCom if needed
        from airflow.operators.python import get_current_context
        context = get_current_context()
        context["ti"].xcom_push(
            key="number_of_people_in_space",
            value=number_of_people_in_space
        )

        return list_of_people_in_space

    # -----------------------------
    # Task 2 – Print details
    # -----------------------------
    @task
    def print_astronaut_craft(greeting: str, person_in_space: dict):
        """
        Print astronaut name + spacecraft.
        Used with dynamic task mapping.
        """
        name = person_in_space["name"]
        craft = person_in_space["craft"]
        print(f"{name} is currently in space flying on the {craft}! {greeting}")

    # -----------------------------------
    # Dynamic Task Mapping
    # -----------------------------------
    astronauts = get_astronauts()

    print_astronaut_craft.partial(
        greeting="Hello! :)"
    ).expand(
        person_in_space=astronauts
    )


# Instantiate the DAG
example_astronauts_taskflow()
