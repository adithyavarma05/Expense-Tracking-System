from fastapi import FastAPI
import db_helper
from datetime import date
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date: date
    end_date: date

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses_for_date(expense_date:date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses
@app.post("/expenses/{expense_date}")
def add_or_update_data(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_into_expenses(expense_date,expense.amount,expense.category,expense.notes)


@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data=db_helper.fetch_data_between_dates(date_range.start_date, date_range.end_date)
    total=sum([row["Total"] for row in data])
    total_percentage_data = {}
    for i,row in enumerate(data):
        percentage=(row["Total"]*100)/total if total!=0 else 0
        total_percentage_data[row["category"]]={
            "Total":row["Total"],
            "Percentage":percentage
        }
    return total_percentage_data

@app.get("/analytics_month/")
def get_month_analytics():
    month_data=db_helper.fetch_data_months()
    return month_data