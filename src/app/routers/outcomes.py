from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db import outcomes as db
from app.models.outcome import Outcome, OutcomeCreate

router = APIRouter(prefix="/outcomes", tags=["outcomes"])

@router.post("/", response_model=Outcome)
async def create_outcome(outcome: OutcomeCreate, session: AsyncSession = Depends(get_session)):
    return await db.create_outcome(session, outcome)

@router.get("/", response_model=list[Outcome])
async def read_outcomes(session: AsyncSession = Depends(get_session)):
    return await db.get_outcomes(session)

@router.get("/{outcome_id}", response_model=Outcome)
async def read_outcome(outcome_id: int, session: AsyncSession = Depends(get_session)):
    db_outcome = await db.get_outcome_by_id(session, outcome_id)
    if not db_outcome:
        raise HTTPException(status_code=404, detail="Outcome not found")
    return db_outcome