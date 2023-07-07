import py3Dmol

pdb_file= 'path/to/your/pdb/file.pdb' # Replace with the path of your pdb file
ligand_residue = 'LIG'                # Replace 'LIG' with the actual residue name of your ligand
active_residues = [102, 154, 178]     # The variable `active_residues_rsv` represents a list of residue numbers that are considered active in the context of the ligand.
                                      # Each residue number corresponds to a specific amino acid residue in a protein structure.

def parse_pdb_atoms(pdb_file):
    atoms = []  # Create an empty list to store the atom information

    with open(pdb_file, 'r') as f:  # Open the PDB file for reading
        for line in f:  # Iterate over each line in the file
            if line.startswith('ATOM'):  # Check if the line starts with 'ATOM'
                atom = {}  # Create an empty dictionary to store the atom details

                # Extract the residue number and remove leading/trailing whitespace
                atom['resi'] = int(line[22:26].strip())

                # Extract the three-letter residue name and remove leading/trailing whitespace
                atom['resn'] = line[17:20].strip()

                atoms.append(atom)  # Add the atom details to the list

    return atoms  # Return the list of atom information


def visualize_pdb_with_ligand(pdb_file, ligand_residue, active_residues):
    # Create the Py3Dmol viewer object
    viewer = py3Dmol.view(width=600, height=400)
    
    # Load the receptor PDB file
    viewer.addModel(open(pdb_file, 'r').read(), 'pdb')

    # Select ligand atoms
    viewer.setStyle({'resn': ligand_residue}, {'stick': {'colorscheme': 'greenCarbon'}})

    # Set the receptor visualization style
    viewer.setStyle({'chain': 'A'}, {'cartoon': {'color': 'lightgrey'}})

    # Highlight active residues based on residue numbers
    viewer.setStyle({'resi': active_residues}, {'stick': {'colorscheme': 'lightgreyCarbon'}})

    # Add labels to ligand residue
    viewer.addLabel(f'{ligand_residue} ({ligand_residue})', {'fontColor': 'black', 'backgroundColor': 'white', 'fontSize': 10.5}, {'resn': ligand_residue})

    # Parse atom information from the PDB file
    atoms = parse_pdb_atoms(pdb_file)

    # Add labels to active residues
    for residue_num in active_residues:
        for atom in atoms:
            if atom['resi'] == residue_num:
                residue_name = atom['resn']
                viewer.addLabel(f'{residue_name} ({residue_num})', {'fontColor': 'black', 'backgroundColor': 'white', 'fontSize': 8.5}, {'resi': residue_num})
                break

    # Set the view to focus on the ligand
    viewer.zoomTo({'chain': 'A', 'resn': ligand_residue})

    # Display the viewer
    viewer.show()

visualize_pdb_with_ligand(pdb_file, ligand_residue, active_residues)
