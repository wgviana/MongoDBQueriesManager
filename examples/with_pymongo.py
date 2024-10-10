#!/usr/bin/env python3
# Copyright (c) Modos Team, 2021

from __future__ import annotations

from typing import Any

from pymongo import MongoClient

from mongo_queries_manager import mqm


if __name__ == "__main__":
    client: MongoClient[dict[str, Any]] = MongoClient("localhost", 27017)
    db = client["test-database"]
    collection = db["test-collection"]

    mongodb_query = mqm(
        string_query=(
            "frequency>5&text$=itaú&context=labflix,omnijs&fk_project=628948&remove=numbers&alpha=/itaú/i,/bradesco/i"
        )
    )

    result = collection.find(**mongodb_query)
