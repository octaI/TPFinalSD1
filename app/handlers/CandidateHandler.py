from typing import List

from app.model.Candidate import Candidate


def get_all_candidates():
    candidates: List[Candidate] = Candidate.find_all()
    return {
        "count": len(candidates),
        "candidates": [c.to_dict() for c in candidates]
    }
