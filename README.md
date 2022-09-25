# Audit Log Service

**Audit Log Service** - Audit logging is the process of documenting activity within the software systems used across your organization. Audit logs record the occurrence of an event, the time at which it occurred, the responsible user or service, and the impacted entity[1].


**Functional Requirements**

| Req Code      | Requirement                        | 
| ------------- |:----------------------------------:|
| ALS_01        | Accept data from systems           | 
| ALS_02        | Save data from other systems       |
| ALS_03        | Serve data through http endpoint   |
| ALS_04        | Authentication for all operations  | 
| ALS_05        | Deploy service as HTTP Server      |


**Design Specifications**


| Req Code      | Requirement                                          | 
| ------------- |:----------------------------------------------------:|
| ALS_01        | Send data to Server through post request             | 
| ALS_02        | Save data to SQL database                            |
| ALS_03        | Serve data through http endpoint                     |
| ALS_04        | Employ Token Authentication from chosen frameworks   | 
| ALS_05        | Local Deployment                                     |



**Framework Overview**

The basis overview of the server is shown below. 

![Basic Architecture Overview](images/Audit_Log_Service.png)

The API Sequence Diagram for the log service is shown below. 

![Basic Architecture Overview](images/Sequence_Diagram.png)

**Software and Technologies proposed for solution**

| Design Specification ID     | Solution.                                  | 
| --------------------------- |:------------------------------------------:|
| ALS_01                      | Use FLASK Web Framework                    | 
| ALS_02                      | Use SQLite Database Engine                 |
| ALS_03                      | Deploy locally through FLASK web framework |
| ALS_04                      | Flask HTTP Token Authentication            | 
| ALS_05                      | Deploy locally through FLASK web framework |







**References**

[1] https://www.datadoghq.com/knowledge-center/audit-logging/

