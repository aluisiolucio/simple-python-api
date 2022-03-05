from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from src.entities.people import People

from ext.database import connection

templates = Jinja2Templates(directory="templates")

def post_people(form):    
    people = People()
    people.name = form['name']
    people.age = form['age']
    people.birthday = form['birthday'].isoformat()
    
    db_connect = connection()
    
    try:
        db_connect.add(people)
        db_connect.commit()
    except:
        raise HTTPException(status_code=500, detail="Error persisting data in database") 
    
    return RedirectResponse('/', status_code=status.HTTP_302_FOUND)

def get_people(request):
    db_connect = connection()
    
    people = db_connect.query(People).order_by(People.name).all()
    
    for person in people:
       person.birthday = person.birthday.strftime("%m/%d/%Y")
    
    return templates.TemplateResponse("index.html", {"request": request, "people": people})