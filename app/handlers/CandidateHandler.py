from typing import List

from app.model.Candidate import Candidate
from app.model.Vote import Vote


def get_all_candidates(request):
    candidates: List[Candidate] = Candidate.find_all()
    return {
        "count": len(candidates),
        "candidates": [c.to_dict() for c in candidates]
    }


def get_one_candidate(request):
    candidate = Candidate.find_candidate(request.args.get('full_name'))
    votes = Vote.get_candidate_votes(candidate[0].id)
    print(votes)
    return{
        "candidate": candidate[0].to_dict(),
        "total_votes": len(votes)
    }

def get_all_votes(request):
    votes: List[Vote] = Vote.get_all()
    return  {
        "count": len(votes),
        "votes": [v.to_dict() for v in votes]
    }

def insert_candidate_vote(request):
    candidate_id = request.form['candidate_id']
    returned_id = Vote.insert_vote(candidate_id)
    return {
        "vote_id" : returned_id
    }


def add_candidate(request):
    data = request.json
    return Candidate.create(data)
