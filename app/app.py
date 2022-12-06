#!/usr/bin/env python3.9
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from commons.constants import embed_component
from commons.textformat import txt,txt2,txt3

st.set_page_config(page_title='Ernesto Crespo\'s resume' ,layout="wide",page_icon='👨‍🔬')

with open("/app/commons/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    
#####################
# Header 
st.sidebar.write('''
# Ernesto Crespo.
##### *Resume* 
''')

image = Image.open('/app/commons/ec.jpg')
st.sidebar.image(image, width=130)

st.sidebar.markdown('## Summary', unsafe_allow_html=True)
st.sidebar.info('''
- Electrical Engineer.
- Python Developer.
''')
with st.sidebar:
        components.html(embed_component['linkedin'],height=270)

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: ecrespo@gmail.com')
pdfFileObj = open('/app/pdfs/ErnestoCrespo.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='ErnestoCrespo.pdf',mime='pdf')
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


with open("/app/commons/nav.md") as f:
    st.markdown('{}'.format(f.read()), unsafe_allow_html=True)


st.markdown('''
## Education
''')

txt('**Electrical Engineer**, *Carabobo University*, Venezuela',
'2001')

#####################
st.markdown('''
## Work Experience
''')

txt('**Software Engineer III - Backend Developer**, *Asistensi Global Insurance, Inc.* ',
'Jul2022-present')
st.markdown('''
- Improved 50% (backend only for now) of the engineering software process in EMS emergency management systems by developing Python Clean code validation.
- Reduce response times through bug fixes and support services for the medical emergency management tool.

Tech Stack: Django, Django-rest framework, postgreSQL, Docker, AWS Lambda, Python, pandas, numpy, FastAPI.

''')

txt('**Lead Software Engineer - Team Lead EMS**, *Asistensi Global Insurance, Inc.* ',
'Oct2021-Jul2022')
st.markdown('''
- Reduce response times through bug fixes and support services for the medical emergency management tool.
- Improve the medical prescription service for Asistensi clients in Mexico by 60% through the design and development of the Medikit API integration with EMS.

Tech Stack: Django, Django-rest framework, postgreSQL, Docker, AWS S3, AWS Lambda, Python, pandas, numpy.
''')

txt('**AWS Cloud Engineer**, *Escala24x7*',
'Aug2019-Oct2021')
st.markdown('''
- Improved customer service by 80% by developing AWS APIs and automating Escala customer service.
- Improved 90% of bank customer call searches by developing a data lake for Banesco's call system.
- Improved 80% of vehicle credit sales inquiries and customer delinquencies by developing a data lake that analyzes vehicle monitoring system data.

Tech Stack: Python, pandas, numpy, S3, DynamoDB, RDS, lambda, cloudwatch Event, SNS, SQS, AWS API, step functions, cloud training, AWS SAM, AWS Athena, AWS Glue, AWS Redshift.

''')

txt('**BI DeveloperBI Developer**, *Troc Global*',
'Jul2018-Aug2019')
st.markdown('''
- Accelerated the decision making of the company's management through the development of modules and APIs for EDA, PCA and predictive analysis as a tool for decision making in the management of electronic and mobile equipment sales stores in Walmart establishments.

Tech Stack: Python, pandas, numpy, scikit-learn, pyMC3, matplotlib, Seaborn, Django-rest framework, postgresql, and rethinkDB.* Accelerated the decision making of the company's management through the development of modules and APIs for EDA, PCA and predictive analysis as a tool for decision making in the management of electronic and mobile equipment sales stores in Walmart establishments. Tech Stack: Python, pandas, numpy, scikit-learn, pyMC3, matplotlib, Seaborn, Django-rest framework, postgresql, and rethinkDB.
''')

txt('**Senior Analyst**, *PDVSA Oil Company*',
'May2016-Sep2018')
st.markdown('''
- Developed geochemical analysis Web application to estimate the presence of compartments in oil fields. * Digital oil field proof of concept. * Architecture designed for web Scada.

Tech Stack: MongoDB, PostgreSQL, Python, Flask, Pandas, numpy, sciPy
''')

txt('**Maitenance Analyst**, *PDVSA Oil Company*',
'Nov2014-Apr2016')
st.markdown('''
- Network technical support,
- Gasoline distribution system.

Tech Stack: Linux, Python, bash, sql
''')

txt('**Technology Manager**, *Infocentro Foundation*',
'Jan2014-Jun2014')
st.markdown('''
Lead teams of:

- Development of administrative systems
- Server management
- Technical supportLead teams of: * Development of administrative systems * Server management * Technical support

Skills: API RestFull en Django y Python(Tastypie, django-rest-framework, Eve)
''')

txt('**Software Developer**, *Cenditel*',
'Jul2011-Aug2012')
st.markdown('''
- I developed an application to send text messages from Linux using Python
- Live-cd for managing radio stations

Tech stack: Debian, bash, Python, GTK, Debian live, Debian package
''')

txt('**Systems Administrator**, *0269*',
'Nov2010-May2011')
st.markdown('''

Implementation of security services:
- firewalls,
- Proxy management and content filtering.
- Network monitoring
- Instruction Detection System
- Anti-spam gateway
- VPN

Tech Stack: Iptables, bash, Python, Debian, Linux, Ntop, postfix, spamassasin, nagios, squid, squidGuard. OpenVPN and Snort
''')

txt('**Linux Instructor**, *AIT DST PDVSA*',
'Apr2010-Nov2010')
st.markdown('''

- Debian Linux Instructor for the Scada DST project

Tech Stack: Debian Linux, network managemente.
''')

txt('**Software Architect**, *AIT DST PDVSA*',
'Apr2010-Aug2010')
st.markdown('''

- Design of new architecture for the project Simulation of Gas Pipeline Networks in real-time.

''')

txt('**Systems Administrator**, *AIT DST PDVSA*',
'Jan2007-Jul2010')
st.markdown('''
Implemented:

- Firewalls
- VPN
- file server
- proxy server
- Web server
- Instruction Detection System

Tech Stack: Debian, Apache, Samba, Squid, SquidGuard, Nagios, Iptables and OpenVPN, Snort
''')

txt('**Team Lead**, *AIT DST PDVSA*',
'Jan2010-Jun2010')
st.markdown('''
* Developed Live-CD Linux for blind people

Tech Stack: Python, Debian live-cd, bash, GTK, Debian custom package* Developed Live-CD Linux for blind people Tech Stack: Python, Debian live-cd, bash, GTK, Debian custom package

''')

txt('**Team Lead**, *AIT DST PDVSA*',
'Dec2009-Apr2010')
st.markdown('''
Leading the Gas Pipeline Network Simulation Project in real-time

Tech Stack: Fortran, C++, GTK, postgreSQL

''')

txt('**Team Lead**, *AIT DST PDVSA*',
'Dec2009-Apr2010')
st.markdown('''
Leading the Gas Pipeline Network Simulation Project in real-time

Tech Stack: Fortran, C++, GTK, postgreSQL

''')

txt('**Team Lead**, *Fundabit*',
'Jun2006-Mar2007')
st.markdown('''
- Authoring tool developed for teaching.
''')

txt('**Technology Advisor**, *Fundabit*',
'Mar2005-Nov2005')
st.markdown('''
- Development of the Fundabit Educational Portal.

Technology stack: CMS mambo PHP, Linux, Apache, mod_security
''')

txt('**Professor**, *José Antonio Páez University*',
'Aug2002-Feb2005')
st.markdown('''
- Computer network
- Informatic security
- System administration
''')

txt('**Network and Systems Administrator**, *José Antonio Páez University*',
'Jan2002-Jul2004')
st.markdown('''

Implemented:
- Email server
- Proxy server
- File server
- Printer server
- Web server
Tech Stack: Fedora, Sendmail, Squid, SquidGuard, Samba, NFS, CUPS, Apache.
''')

txt('**Professor**, *Carabobo University*',
'Mar2001-Aug2001')
st.markdown('''
- Digital Logic Laboratory
''')

txt('**Teacher Assistant**, *Carabobo University*',
'May1998-Aug2001')
st.markdown('''
- Computer Architecture
- Digital Computing I
- Digital Computing II
''')



#####################
st.markdown('''
## Portfolio

#### Notebooks

##### EDAs

* [Climate Change Temperature by Country, Global Temperature and CO2 ppm](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/Climate_change.ipynb)

* [Exploring Covid19 data with pandas](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/covid19-6.ipynb)

* [Analysis of the 25 largest retailers in the United States](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/Retailers_US.ipynb)

* [Analysis Stanford Open Policy Project Dataset](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/police_traffic.ipynb)

* [Investigating Netflix Movies and Guest Stars in The Office](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/Netflix.ipynb)

##### Graphs

* [Matplotlib](https://github.com/ecrespo/data_science_portfoliio/blob/main/notebooks/Matplotlib.ipynb)
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Javascript`, `Julia`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Dashboard', '`Streamlit`, `Tableu`,`Power BI`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`,`Keras`')
txt3('Web development', '`Django`, `FastAPI`, `HTML`, `CSS`')
txt3('Model deployment', '`Heroku`, `AWS`, `Digital Ocean`')
txt3('Operating System', '`Linux`, `Window`')


skills = {
    'Programming': {'Python':5, 'R':2, 'Javascript':2,'Julia':1},
    'Data processing/wrangling':{ 'SQL':3, 'pandas':5, 'numpy':5},
    'Data visualization':{ 'matplotlib':5, 'seaborn':4, 'plotly':3},
    'Dashboard': {'Streamlit': 4,'Tableu':2,'Power BI': 1},
    'Machine Learning/Deep Learning': {'scikit-learn':3,'TensorFlow':2,'Keras':1},
    'Web development': {'Django':4, 'FastAPI':3, 'Flask':2,'HTML':2, 'CSS':2},
    'Operating System':  {'Linux':5, 'Window':3,'MacOs':2}
}

list_skills = list(skills.keys())

select_skills = st.selectbox(
        "Skills", list_skills
    )

#st.text(f"{select_skills}")


df = pd.DataFrame(dict(
    r=list(skills[select_skills].values()),
    theta=list(skills[select_skills].keys())))

#st.write(df)


fig = px.line_polar(df, r='r', theta='theta', line_close=True,markers=True,title=select_skills)
fig.update_traces(fill='toself')
# fig.show()
st.plotly_chart(fig, use_container_width=True)

st.text("Comparative")
fig2 = go.Figure()

for key,value in skills.items():
    
    fig2.add_trace(go.Scatterpolar(
        r=list(value.values()),
        theta=list(value.keys()),
        fill='toself',
        name=key
    ))

fig2.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True
)

st.plotly_chart(fig2, use_container_width=True)
#####################
st.markdown('''
## Social Media
''')
txt2('Medium', 'https://seraph13.medium.com/')
txt2('LinkedIn', 'https://www.linkedin.com/in/ernestocrespo/?locale=en_US')
txt2('Twitter', 'https://twitter.com/_seraph1')
txt2('GitHub', 'https://github.com/ecrespo')
txt2('Gitlab', 'https://gitlab.com/ecrespo')
txt2('Blog', 'https://blog.seraph.to')


#####################
st.markdown('''
## Certifications
''')

with st.spinner(text="Building line"):
    with open('/app/commons/timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)
        
