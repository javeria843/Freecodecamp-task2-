import pandas as pd
def calculate_demographic_data(print_data=True):
    df=pd.read_csv("adult.csv")
    race_count=df['race'].value_counts()
    average_age=round(df[df['sex']=='Male']['age'].mean(),1)

    percentage_bachlors=round((df['education']=='Bachlors').mean()*100,1)
    advanced_education= df['education'].isin(['Bachlors','Masters','Doctorate'])
    higher_education_rich=round((df[advanced_education]['salary']=='>50k').mean()*100,1)
    lower_education = ~advanced_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    country_stats=df[df['salary']=='>50K']['native-country'].value_counts()/df['native-country'].value_counts()
    highest_earning_country=country_stats.idxmax()
    highest_earning_country_percentage= round(country_stats.max() *100,1)
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    if print_data:
        print("Race Count:\n", race_count)
        print("Average Age of Men:", average_age)
        print("Percentage with Bachelors:", percentage_bachlors)
        print("Higher Ed Rich %:", higher_education_rich)
        print("Lower Ed Rich %:", lower_education_rich)
        print("Min Work Hours:", min_work_hours)
        print("Rich % Among Min Workers:", rich_percentage)
        print("Highest Earning Country:", highest_earning_country)
        print("Highest Earning %:", highest_earning_country_percentage)
        print("Top Occupation in India (>50K):", top_IN_occupation)

        return{
            "race_count":race_count,
            "average_age":average_age,
             "percentage_bachelors":percentage_bachlors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation

        }