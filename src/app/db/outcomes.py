from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession 
from app.models.outcome import OutcomeRecord, OutcomeCreate

async def create_outcome(session: AsyncSession, outcome: OutcomeCreate) -> OutcomeRecord:
    db_outcome = OutcomeRecord.model_validate(outcome)
    session.add(db_outcome)
    await session.commit()
    await session.refresh(db_outcome)
    return db_outcome

async def get_outcomes(session: AsyncSession) -> list[OutcomeRecord]:
    statement = select(OutcomeRecord)
    result = await session.exec(statement)
    return list(result.all())

async def get_outcome_by_id(session: AsyncSession, outcome_id: int) -> OutcomeRecord | None:
    return await session.get(OutcomeRecord, outcome_id)