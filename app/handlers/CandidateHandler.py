from typing import List

from app.model.Candidate import Candidate


def get_all_candidates(request):
    candidates: List[Candidate] = Candidate.find_all()
    return {
        "count": len(candidates),
        "candidates": [c.to_dict() for c in candidates]
    }


def add_candidate(request):
    data = request.json
    return Candidate.create(data)
