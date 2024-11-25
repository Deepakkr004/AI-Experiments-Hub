# Import necessary libraries from pgmpy
from pgmpy.models import BayesianNetwork # type: ignore
from pgmpy.factors.discrete import TabularCPD # type: ignore
from pgmpy.inference import VariableElimination # type: ignore
 
# Step 1: Create the structure of the Bayesian Network
# (Weather -> Traffic -> Accident)
model = BayesianNetwork([('Weather', 'Traffic'), ('Traffic', 'Accident')])
 
# Step 2: Define the Conditional Probability Distributions (CPDs)
 
# CPD for Weather (P(Weather))
# Weather: Rainy (1) or Not Rainy (0)
cpd_weather = TabularCPD(variable='Weather', variable_card=2, values=[[0.7], [0.3]])
 
# CPD for Traffic given Weather (P(Traffic | Weather))
# Traffic: Light (0) or Heavy (1)
cpd_traffic = TabularCPD(variable='Traffic', variable_card=2,
                         values=[[0.7, 0.2],  # Light, Heavy given Weather (Not Rainy, Rainy)
                                 [0.3, 0.8]],
                         evidence=['Weather'], evidence_card=[2])
 
# CPD for Accident given Traffic (P(Accident | Traffic))
# Accident: No Accident (0) or Accident (1)
cpd_accident = TabularCPD(variable='Accident', variable_card=2,
                          values=[[0.8, 0.1],  # No Accident, Accident given Light, Heavy traffic
                                  [0.2, 0.9]],
                          evidence=['Traffic'], evidence_card=[2])
 
# Step 3: Add the CPDs to the model
model.add_cpds(cpd_weather, cpd_traffic, cpd_accident)
 
# Step 4: Check if the model is valid
assert model.check_model()
 
# Step 5: Perform Inference using Variable Elimination
 
# Create an inference object
inference = VariableElimination(model)
 
# Step 6: Query the probability of Accident given that Weather is Rainy (Weather = 1)
query_result = inference.query(variables=['Accident'], evidence={'Weather': 1})
 
# Print the result of the inference
print(query_result)