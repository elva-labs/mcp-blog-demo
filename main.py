from fastmcp import FastMCP
from typing import Dict, Optional, Union
from candidates import CANDIDATES

# Initialize the MCP server
mcp = FastMCP("Candidate Search")

@mcp.tool
def search_candidates(
    skill: Optional[str] = None,
    min_experience: Optional[Union[str, int]] = None,
    max_rate: Optional[Union[str, int]] = None,
    location: Optional[str] = None,
    availability: Optional[str] = None,
    specialization: Optional[str] = None
) -> Dict:
    """
    Search for candidates based on various criteria.
    
    Args:
        skill: Search for candidates with a specific skill (case-insensitive)
        min_experience: Minimum years of experience required
        max_rate: Maximum hourly rate in USD
        location: Filter by location (partial match, case-insensitive)
        availability: Filter by availability (e.g., "Immediate", "2 weeks")
        specialization: Search for specific specialization area
    
    Returns:
        A dictionary containing matching candidates and search metadata
    """
    results = CANDIDATES.copy()
    
    # Convert string inputs to integers if needed
    if min_experience is not None and isinstance(min_experience, str):
        try:
            min_experience = int(min_experience)
        except ValueError:
            min_experience = None
    
    if max_rate is not None and isinstance(max_rate, str):
        try:
            max_rate = int(max_rate)
        except ValueError:
            max_rate = None
    
    # Apply filters
    if skill:
        skill_lower = skill.lower()
        results = [c for c in results if any(skill_lower in s.lower() for s in c["skills"])]
    
    if min_experience is not None:
        results = [c for c in results if c["experience_years"] >= min_experience]
    
    if max_rate is not None:
        results = [c for c in results if c["rate"] <= max_rate]
    
    if location:
        location_lower = location.lower()
        results = [c for c in results if location_lower in c["location"].lower()]
    
    if availability:
        availability_lower = availability.lower()
        results = [c for c in results if availability_lower in c["availability"].lower()]
    
    if specialization:
        spec_lower = specialization.lower()
        results = [c for c in results if any(spec_lower in s.lower() for s in c["specializations"])]
    
    # Sort by experience (descending)
    results.sort(key=lambda x: x["experience_years"], reverse=True)
    
    return {
        "total_found": len(results),
        "search_criteria": {
            "skill": skill,
            "min_experience": min_experience,
            "max_rate": max_rate,
            "location": location,
            "availability": availability,
            "specialization": specialization
        },
        "candidates": results
    }

@mcp.tool
def get_candidate_details(candidate_id: Union[str, int]) -> Optional[Dict]:
    """
    Get detailed information about a specific candidate by ID.
    
    Args:
        candidate_id: The unique identifier of the candidate
    
    Returns:
        Detailed candidate information or None if not found
    """
    # Convert string input to integer if needed
    if isinstance(candidate_id, str):
        try:
            candidate_id = int(candidate_id)
        except ValueError:
            return None
    
    for candidate in CANDIDATES:
        if candidate["id"] == candidate_id:
            return {
                "candidate": candidate,
                "summary": f"{candidate['name']} is a {candidate['title']} with {candidate['experience_years']} years of experience, "
                          f"currently based in {candidate['location']}. "
                          f"Rate: ${candidate['rate']}/hour. Availability: {candidate['availability']}."
            }
    return None

@mcp.tool
def list_all_skills() -> Dict:
    """
    Get a list of all unique skills in the candidate database.
    
    Returns:
        Dictionary with all unique skills and their frequency
    """
    skill_count = {}
    for candidate in CANDIDATES:
        for skill in candidate["skills"]:
            skill_count[skill] = skill_count.get(skill, 0) + 1
    
    # Sort by frequency
    sorted_skills = dict(sorted(skill_count.items(), key=lambda x: x[1], reverse=True))
    
    return {
        "total_unique_skills": len(sorted_skills),
        "skills": sorted_skills
    }

if __name__ == "__main__":
    mcp.run()