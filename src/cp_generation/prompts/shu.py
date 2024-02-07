from .prompt_template import *


rule = """● Elemental Selection: Choose elements that form a single-phase solid solution or a simple eutectic system. The elements Al, Co, Cr, Fe, Ni are commonly used in EHEAs due to their compatibility and ability to form stable high-entropy mixtures. 
●  Optional Elements Effect: Cu enhances corrosion resistance and conductivity but may lower thermal stability. Mn alters fluidity and solidification, risking casting defects and phase instability, leading to unwanted phases or microstructures.
●  Atomic Size Difference: The atomic radii of the constituent elements should differ by a margin of 5% to 15%, a range that assists in maintaining a stable solid solution while simultaneously minimizing lattice distortion.
●  Valence Electron Concentration (VEC): The VEC should be in a range that favors the formation of desired phases (like FCC, BCC, or HCP). The phase stability in high entropy alloys is often influenced by the electron concentration. 
●  Mixing Enthalpy: Select elements with negative or low positive mixing enthalpies to promote solid solution formation and reduce the tendency for intermetallic compound formation.
●  Advancing Green Manufacturing: To maintain the intrinsic strength and castability of eutectic high entropy alloys with minimal heat treatment and post-processing, adherence to green manufacturing principles is essential, streamlining the production process.
●  Phase Diagram Analysis: Identify eutectic points where a simple solid solution or a combination of phases (like FCC+B2) can form. Look for compositions that avoid brittle intermetallic phases. Select compositions near eutectic points that favor the formation of desired solid solution phases. 
● Weighted Average Physical Properties: Consider the weighted average of physical properties like melting point, density, and elasticity of the constituent elements."""
prompt = CustomPromptTemplate.from_template("""Review the provided literature to determine its relevance to key aspects of eutectic high entropy alloy design. Add it to the knowledge base for inverse design rules if relevant. The literature should partially or fully relate to these key points:

Key Points:
1. Inclusion of elements Al, Co, Cr, Fe, Ni (mandatory) and Mu, Cu (optional) in the eutectic high entropy alloy.
2. Process features like cold rolling, heat treatment temperature, and time.
3. Focus on high UTS (Ultimate Tensile Strength) and EL (Elongation) in eutectic high entropy alloy design.

Output format:
- {{"Relevance": 1}} (for high relevance, suitable for the knowledge base)
- {{"Relevance": 0}} (for low relevance, unsuitable for the knowledge base)

Document details:
- Title: {title}
- Abstract: {abstract}

Please output either {{"Relevance": 1}} or {{"Relevance": 0}}, without providing reasons or restating the information from the document I provided.""")
   