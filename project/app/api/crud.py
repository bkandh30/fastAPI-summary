from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

from typing import Union
from typing import List
from fastapi import HTTPException

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url = payload.url,
        summary = "dummy summary"
    )

    await summary.save()
    return summary.id

async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if not summary:
        return HTTPException(status_code=404, detail="Summary not found")
    return summary


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries

