# Tables
- [Sources](#1---sources)
- [Agents](#2---agents)
- [Projects](#3---projects)
- [Data](#4---data)
- [Leads](#5---Leads)
- [Live_Data](#6---livedata)

# Tables Details

####  1 - Sources
- id 
- source_name
- deleted
- active 
- adding_date
- adding_time

===> Query :
```sql
CREATE TABLE "Sources" (
	"id" integer not null PRIMARY KEY AUTOINCREMENT , 
  	"source_name" varchar(50) not NULL ,
  	"deleted" intger DEFAULT 0 ,
  	"active" intger DEFAULT 1 ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```

####  2 - Agents 
- id
- agent_name
- deleted
- active 
- adding_date
- adding_time

===> Query :
```sql
CREATE TABLE "Agents" (
	"id" integer not null PRIMARY KEY AUTOINCREMENT , 
  	"agent_name" varchar(50) not NULL ,
  	"deleted" intger DEFAULT 0 ,
  	"active" intger DEFAULT 1 ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```


####  3 - Projects 
- id
- project_name
- deleted
- active 
- extension
- adding_date
- adding_time


===> Query :
```sql
CREATE TABLE "Projects" (
	"id" integer not null PRIMARY KEY AUTOINCREMENT , 
  	"project_name" varchar(50) not NULL ,
  	"deleted" intger DEFAULT 0 ,
  	"active" intger DEFAULT 1 ,
	"extension" intger ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```

####  4 - Data
- number
- source_id
- name (optional)
- taken
- deleted
- registered
- adding_date
- adding_time

===> Query :
```sql
CREATE TABLE "Data" (
	"number" varchar(20) NOT NULL UNIQUE ,
  	"source_id" intger not NULL REFERENCES "Sources"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"name" varchar(30) NULL ,
  	"taken" intger DEFAULT 0 ,
  	"deleted" intger DEFAULT 0 ,
  	"registered" intger DEFAULT 0 ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```


#### 5 - Leads

- agent_id
- number
- name
- project_id
- source_id
- description
- adding_date
- adding_time


===> Query :
```sql
CREATE TABLE "Leads"(
	"agent_id" intger not NULL REFERENCES "Agents"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"number" varchar(20) NOT NULL ,
  	"name" varchar(30) NULL ,
  	"project_id" intger not NULL REFERENCES "Projects"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"source_id" intger not NULL REFERENCES "Sources"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"description" varchar(500) NULL ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```                                                

#### 6 - Live_Data

- agent_id
- number
- project_id
- source_id
- adding_date
- adding_time

===> Query :
```sql
CREATE TABLE "Live_Data"(
	"agent_id" intger not NULL REFERENCES "Agents"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"number" varchar(20) NOT NULL ,
  	"project_id" intger not NULL REFERENCES "Projects"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"source_id" intger not NULL REFERENCES "Sources"("id") DEFERRABLE INITIALLY DEFERRED ,
  	"adding_date" date  DEFAULT CURRENT_DATE ,
	"adding_time" time  DEFAULT CURRENT_TIME
);
```                                                
