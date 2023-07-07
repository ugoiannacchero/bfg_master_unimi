I used py3Dmol to generate a function that allows the visualization of ligand-protein complexes from a pdb file.

You can see an example of how this function works in [StructuralBiology_JC](StructuralBiology_JC.ipynb) where I visualize two docked ligand-protein complexes generated my by groupmates of a Strucutral Biology journal club of the BFG master. Click on open in Colab to visualize the structures.

#### Requirements:

Requires py3Dmol library
```
import py3Dmol
```
A protein structure with the ligand is required. One can try using a structure directly obtained from [Protein Data Bank](https://www.rcsb.org).

#### Necessary arguments:

```
pdb_file = 'path/to/your/pdb/file.pdb'
ligand_residue = 'LIG'
active_residues = [102, 154, 178] 
```

`pdb_file= 'path/to/your/pdb/file.pdb'` replace with the path of your pdb file
<br>
`ligand_residue = 'LIG'` replace 'LIG' with the actual residue name of your ligand
<br>
`active_residues= [102, 154, 178]` generates a list of residue numbers that are considered active in the context of the ligand.
Each residue number corresponds to a specific amino acid residue in a protein structure. 102, 154 and 170 are just an example.
______________________________________________________________________________________________________________________________

#### pars_pdb_atoms function:

```
def parse_pdb_atoms(pdb_file):
    atoms = [] 
    with open(pdb_file, 'r') as f:
        for line in f: 
            if line.startswith('ATOM'): 
                atom = {}  
                atom['resi'] = int(line[22:26].strip())
                atom['resn'] = line[17:20].strip()
                atoms.append(atom)
    return atoms
```

The `parse_pdb_atoms` function parses a PDB file and extracts the residue numbers and residue names of the atoms, storing them in a list of dictionaries.
<br>
Here's how it works:
* It initializes an empty list called `atoms` to store the atom information.
* It opens the specified PDB file in read mode using a `with` statement, which ensures the file is properly closed after reading.
* It iterates over each line in the file using a `for` loop.
* For each line, it checks if the line starts with the keyword 'ATOM' using the `startswith` method.
* If the line starts with 'ATOM', it creates an empty dictionary called `atom` to store the details of the current atom.
* It extracts the residue number from the line, which represents the position of the atom within the protein structure. The residue number is converted to an integer and stored in the `resi` key of the `atom` dictionary.
* It extracts the three-letter residue name, which represents the type of residue the atom belongs to. The residue name is stored in the `resn` key of the `atom` dictionary.
* The `atom` dictionary is appended to the `atoms` list.
* After iterating through all the lines in the file, the function returns the `atoms` list containing the atom information.

 ______________________________________________________________________________________________________________________________

 #### visualize_pdb_with_ligand function:

```
def visualize_pdb_with_ligand(pdb_file, ligand_residue, active_residues):
    viewer = py3Dmol.view(width=600, height=400)
    viewer.addModel(open(pdb_file, 'r').read(), 'pdb')
    viewer.setStyle({'resn': ligand_residue}, {'stick': {'colorscheme': 'greenCarbon'}})
    viewer.setStyle({'chain': 'A'}, {'cartoon': {'color': 'lightgrey'}})
    viewer.setStyle({'resi': active_residues}, {'stick': {'colorscheme': 'lightgreyCarbon'}})
    viewer.addLabel(f'ligand_name', {'fontColor': 'black', 'backgroundColor': 'white', 'fontSize': 10.5}, {'resn': ligand_residue})
    atoms = parse_pdb_atoms(pdb_file)
    for residue_num in active_residues:
        for atom in atoms:
            if atom['resi'] == residue_num:
                residue_name = atom['resn']
                viewer.addLabel(f'{residue_name} ({residue_num})', {'fontColor': 'black', 'backgroundColor': 'white', 'fontSize': 8.5}, {'resi': residue_num})
                break
    viewer.zoomTo({'chain': 'A', 'resn': ligand_residue})
    viewer.show()
visualize_pdb_with_ligand(pdb_file, ligand_residue, active_residues)
```
The function `visualize_pdb_with_ligand` is used to visualize a protein structure (PDB file) with a specific ligand and highlight active residues. 
<br>
Here's how it works:
1. It creates a Py3Dmol viewer object, which will be used to display the visualization.
2. The function loads the receptor PDB file and adds it as a model to the viewer.
3. It selects and styles the ligand atoms based on the provided ligand residue name.
4. The function sets the visualization style for the receptor (non-ligand) using a cartoon representation.
5. Active residues, specified by their residue numbers, are highlighted using a stick representation.
6. Labels are added for the ligand residue and the active residues, displaying their names and numbers.
7. The atom information from the PDB file is parsed using the `parse_pdb_atoms` function (which is assumed to be defined elsewhere).
8. Labels are added for the active residues based on their residue numbers and names obtained from the parsed atom information.
9. The view is set to focus on the ligand.
10. The viewer is displayed to show the visualization.
    
To use this function, you need to provide the required arguments: `pdb_file` (the path to the PDB file), `ligand_residue` (the name of the ligand residue), and `active_residues` (a list of active residue numbers). Once you call the function with the appropriate arguments, it will generate the protein-ligand visualization using Py3Dmol. Within the function `f'ligand_name'` is used as the label for the ligand residue in the visualization, it has to be replaced with the actual name of the ligand you want to display.
_________________________________________________________________________________________________________________________
