{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "68db8144",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f2b05434",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5d9b95dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4882b845",
   "metadata": {},
   "outputs": [],
   "source": [
    "#engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\", connect_args={\"check_same_thread\": False})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e40d5e14",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "aa975973",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "19756257",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6082345f",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4ad08d12",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e1c508b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1a08ef23",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (Temp/ipykernel_17260/3459658878.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\chara\\AppData\\Local\\Temp/ipykernel_17260/3459658878.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    @app.route(\"\\api\\v1.0\\precipitation\")\u001b[0m\n\u001b[1;37m                                         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"\\api\\v1.0\\precipitation\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1c511817",
   "metadata": {},
   "outputs": [],
   "source": [
    "def precipitation():\n",
    "   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "   precipitation = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date >= prev_year).all()\n",
    "   precip = {date: prcp for date, prcp in precipitation}\n",
    "   return jsonify(precip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "eabd4222",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (Temp/ipykernel_17260/1802364990.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\chara\\AppData\\Local\\Temp/ipykernel_17260/1802364990.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    @app.route(\"/api/v1.0/stations\")\u001b[0m\n\u001b[1;37m                                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/stations\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "baab188d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stations():\n",
    "    results = session.query(Station.station).all()\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations=stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "061a8f04",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (Temp/ipykernel_17260/3710546096.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\chara\\AppData\\Local\\Temp/ipykernel_17260/3710546096.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    @app.route(\"/api/v1.0/tobs\")\u001b[0m\n\u001b[1;37m                                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "fb9b3454",
   "metadata": {},
   "outputs": [],
   "source": [
    "def temp_monthly():\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "    results = session.query(Measurement.tobs).\\\n",
    "      filter(Measurement.station == 'USC00519281').\\\n",
    "      filter(Measurement.date >= prev_year).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps=temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42014c33",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
