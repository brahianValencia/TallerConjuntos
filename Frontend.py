import streamlit as st
from functools import reduce
import OperacionesConjuntos as op
import string


def get_operation_string(operation, set_names):
    if operation == "Union":
        return " ∪ ".join(set_names)
    elif operation == "Intersection":
        return " ∩ ".join(set_names)
    elif operation == "Difference":
        return " - ".join(set_names)
    elif operation == "Symmetric difference":
        return " △ ".join(set_names)
    elif operation == "Subset":
        return " ⊆ ".join(set_names)
    elif operation == "Superset":
        return " ⊇ ".join(set_names)
    else:
        return ""


def perform_set_operation(operation, input_sets):
    """
    Perform the specified set operation on the input sets.
    
    Args:
    operation (str): The set operation to perform ('Union', 'Intersection', or 'Difference').
    input_sets (list): A list of sets to operate on.
    
    Returns:
    set: The result of the set operation.
    """
    if not input_sets:
        return None # This checks if input_sets is empty. If it is, the function returns None.
    
    if operation == "Union":
       #lambda function that takes two sets x and y and returns their union. reduce applies the lambda function to the first two sets in input_sets,
         # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        return reduce(lambda x, y: op.union(x, y), input_sets)
      
    elif operation == "Intersection":
         #lambda function that takes two sets x and y and returns their intersection. reduce applies the lambda function to the first two sets in input_sets,
         # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        return reduce(lambda x, y: op.intersection(x,y), input_sets)
    elif operation == "Difference":
         #lambda function that takes two sets x and y and returns their difference. reduce applies the lambda function to the first two sets in input_sets,
         # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        return reduce(lambda x, y: op.difference(x,y), input_sets)
    elif operation == "Symmetric difference":
        #lambda function that takes two sets x and y and returns their Symmetric difference. reduce applies the lambda function to the first two sets in input_sets,
        # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        return reduce(lambda x, y: op.symmetricDifference(x,y), input_sets)
    elif operation == "Subset":
        #lambda function that takes two sets x and y and returns their subset. reduce applies the lambda function to the first two sets in input_sets,
        # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        if num_sets == 1:
            
            return op.subset(input_sets[0], set())
        else:
            return reduce(lambda x, y: op.subset(x, y), input_sets)
       # return reduce(lambda x, y: op.subset(x,y) if num_sets>1 else  op.subset(x,set()), input_sets)
    elif operation == "Superset":
        #lambda function that takes two sets x and y and returns their superset. reduce applies the lambda function to the first two sets in input_sets,
        # then to the result and the next set, and so on, until all sets in input_sets have been processed.
        if num_sets == 1:
            
            return op.superset(input_sets[0], set())
        else:
         return reduce(lambda x, y: op.superset(x,y), input_sets)

# Set the title of the Streamlit app
st.title("Set Operations")

# Create a dropdown to select the set operation
operation = st.selectbox("Operation:", ["Union", "Intersection", "Difference","Symmetric difference","Subset","Superset"])

# Initialize the state for input sets if it doesn't exist
if 'input_sets' not in st.session_state:
    st.session_state.input_sets = [set(), set()]  # Start with 2 empty sets

# Allow user to specify the number of sets
# Allow user to specify the number of sets
min_sets = 1 if operation in ["Subset", "Superset"] else 2
num_sets = st.number_input("Number of sets", min_value=min_sets, value=max(min_sets, len(st.session_state.input_sets)), step=1)
#num_sets = st.number_input("Number of sets", min_value=2, value=len(st.session_state.input_sets), step=1)

# Adjust the number of sets based on user input
if num_sets > len(st.session_state.input_sets):
    st.session_state.input_sets.extend([set() for _ in range(num_sets - len(st.session_state.input_sets))])  # create new empty sets and add them to the list. This ensures that the number of sets matches what the user wants.
elif num_sets < len(st.session_state.input_sets): #number of sets requested by the user is less than the current number of sets stored.?
    st.session_state.input_sets = st.session_state.input_sets[:num_sets]  # trims st.session_state.input_sets to the desired number.


letters = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
set_names = []

# Display input fields for each set
for i, input_set in enumerate(st.session_state.input_sets): #   goes through each set in st.session_state.input_sets, with i as the index and input_set as the current set.
    
     # Use letters[index] to get the corresponding letter (A, B, C, etc.)
    letter = letters[i] if i < len(letters) else f"Set{i+1}"
    set_names.append(letter)

    input_str = st.text_input(f"Set {letter}", key=f"set_{i}", value=', '.join(map(str, input_set))) #create a string representation of the elements in the input_set, where each element is separated by a comma and a space. 
    
    # Update the input set in session state
    try:
        st.session_state.input_sets[i] = set(elem.strip() for elem in input_str.split(",") if elem.strip()) #updates the corresponding set in st.session_state.input_sets with the elements entered by the user, splitting the input string by commas and removing any leading/trailing spaces.
    except ValueError:
        st.error(f"Invalid input for Set {i+1}. Please enter comma-separated elements.") #: If an error is caught, this line displays an error message to the user.

# Display the operation string
operation_string = get_operation_string(operation, set_names)
st.write(f"Operation to perform: {operation_string}")


if st.button("Compute"):
    input_sets = [s for s in st.session_state.input_sets if s]  # filters out any empty sets from st.session_state.input_sets.  
    if (operation in ["Subset", "Superset"] and len(input_sets) >= 1) or (operation not in ["Subset", "Superset"] and len(input_sets) >= 2): #checks if there are at least two non-empty sets.
        result = perform_set_operation(operation, input_sets)  # calls the perform_set_operation function with the selected operation and the list of non-empty sets.
        if operation != "Subset" and operation != "Superset":
         st.success(f"Result: {{{', '.join(map(str, result))}}}") #If the operation is successful, this line displays the result to the user.
        else:
            if len(input_sets)==1:
              st.success(f"Result: {{{', '.join(map(str, result))}}}")
            else:
              st.success(f"Result: {result}") #If the operation is successful, this line displays the result to the user.

    else:
        if operation in ["Subset", "Superset"]:
            st.warning("Please enter at least one non-empty set.")
        else:
         st.warning("Please enter at least two non-empty sets.") # This displays a warning message to the user.