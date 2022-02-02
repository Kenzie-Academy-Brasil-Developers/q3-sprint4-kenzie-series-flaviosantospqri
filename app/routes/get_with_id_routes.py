from flask import Blueprint, request, jsonify
from http import HTTPStatus
from jinja2 import Undefined
import psycopg2

bp = Blueprint('series_get_id', __name__, url_prefix='/api')

@bp.get('/series/<int:id>')
def select_by_id(id):
   
   conn = psycopg2.connect(host='localhost', database='ka_series_db', user='flavio', password='1234')
   
   
   cur = conn.cursor()

   cur.execute(
    """
    SELECT * FROM ka_series
    WHERE id = (%s);
    """, (id, )
   )

   data = cur.fetchone()
   
   conn.commit()
   cur.close()
   conn.close()

   try:
        FIELDNAMES = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']

        data_factory = dict(zip(FIELDNAMES, data))
        
        return {'Data': data_factory}, HTTPStatus.CREATED
   except:
        return {'msg': {}}, HTTPStatus.NOT_FOUND
   
