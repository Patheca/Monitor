import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import warnings
import datetime
import calendar
import json
import requests
from dash import Dash, dcc, html, Input, Output
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as dt, timedelta

warnings.filterwarnings('ignore')

link = "https://sobre-monitor.readthedocs.io/en/latest/"

st.set_page_config(page_title="Monitor endividamento", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="collapsed", 
                   menu_items={'About': f'Para facilitar a sua análise, todos os valores já estão deflacionados!\n\n'
        f'Quer conferir mais detalhes sobre este projeto ou entrar em contato conosco? [Clique aqui]({link})'})

