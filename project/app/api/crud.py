from typing import List, Union

from fastapi import HTTPException

from app.models.pydantic import SummaryPayloadSchema, SummaryUpdatePayloadSchema
from app.models.tortoise import TextSummary

from app.summarizer import generate_summary

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first()
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryUpdatePayloadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).update(url=payload.url, summary=payload.summary)
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary
    return None
