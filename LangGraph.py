from typing import TypedDict
from langgraph.graph import StateGraph,START,END

#State is the plain Python object that is used to represent the state of the graph. It is a dictionary that contains the following
#every node in the graph is represented as a key in the dictionary, and the value is a list of nodes that are connected to that node.

class PatientState(TypedDict):
    patient_name: str
    pysician_note: str
    cardiologiest_note: str
    surgeon_note: str

 
# a node is just python function that takes a state and returns a new state. The node can also have a name and a description.
def general_physician_node(state : PatientState) -> dict:
    # this node represents the general physician's note
    print("Genaral physician examining:",state['patient_name'])

    notes = "Patient reported chest pain and shortness of breath. Blood pressure is elevated. Recommend further cardiac evaluation."
    return {"pysician_note": notes}


def cardiologist_node(state : PatientState) -> dict:
    # this node represents the cardiologist's note  
    print("Cardiologist examining:",state['pysician_note'])
    notes = "Patient has a history of hypertension and high cholesterol. Recommend for surgery. Patient is at risk for heart disease."
    return {"cardiologiest_note": notes}

def surgeon_node(state : PatientState) -> dict:
    # this node represents the surgeon's note
    print("Surgeon examining:",state['pysician_note'])   
    print("Surgeon examining:",state['cardiologiest_note'])   

    notes="Bypass surgery is recommended. Patient is at risk for heart disease. Patient is at risk for heart attack."
    return {"surgeon_note": notes}


#Build the graph

builder = StateGraph(PatientState)

#Add nodes to the graph first arg is the name, second org is the function
builder.add_node("general_physician",general_physician_node)
builder.add_node("cardiologist", cardiologist_node)
builder.add_node("surgeon", surgeon_node)


#add Edges-defines execution order
builder.add_edge(START,"general_physician")
builder.add_edge("general_physician","cardiologist")
builder.add_edge("cardiologist","surgeon")
builder.add_edge("surgeon",END)


#Compile the graph into runnable
graph=builder.compile()

#pass in the initial state to the graph and run it
initial_state = {
    "patient_name": "John Doe", 
    "pysician_note": "",            #will be filled by node 1
    "cardiologiest_note": "",       #will be filled by node 2
    "surgeon_note": ""}             #will be filled by node 3

final_state = graph.invoke(initial_state)

print(final_state)