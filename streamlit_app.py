import streamlit as st
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset with correct column names
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ]

    df = pd.read_csv("adult.csv", header=None, names=column_names, na_values=' ?')
    df.dropna(inplace=True)

    # Calculate metrics
    race_count = df["race"].value_counts()
    average_age = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]["salary"] == ">50K").mean() * 100, 1)
    lower_education_rich = round((df[lower_education]["salary"] == ">50K").mean() * 100, 1)

    min_work_hours = df["hours-per-week"].min()
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    country_stats = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack().fillna(0)
    highest_country = country_stats[">50K"].idxmax()
    highest_country_percentage = round(country_stats[">50K"].max() * 100, 1)

    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"]
        .value_counts().idxmax()
    )

    if print_data:
        print("Race Count:\n", race_count)

    return {
        "race_count": race_count,
        "average_age": average_age,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_country,
        "highest_earning_country_percentage": highest_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }


# STREAMLIT UI
st.title("Demographic Data Analyzer")

result = calculate_demographic_data(print_data=False)

st.header("Race Count")
st.write(result["race_count"])

st.header("Average Age of Men")
st.write(result["average_age"])

st.header("Percentage with Bachelors Degree")
st.write(f"{result['percentage_bachelors']}%")

st.header("Higher Education Rich %")
st.write(f"{result['higher_education_rich']}%")

st.header("Lower Education Rich %")
st.write(f"{result['lower_education_rich']}%")

st.header("Minimum Work Hours")
st.write(result["min_work_hours"])

st.header("Percentage of Rich among Minimum Hour Workers")
st.write(f"{result['rich_percentage']}%")

st.header("Country with Highest Percentage of Rich People")
st.write(f"{result['highest_earning_country']} ({result['highest_earning_country_percentage']}%)")

st.header("Top Occupation in India among Rich")
st.write(result["top_IN_occupation"])
