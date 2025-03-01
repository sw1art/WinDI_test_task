from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict

router = APIRouter()
active_connections: Dict[int, WebSocket] = {}  # user_id -> WebSocket


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    active_connections[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Сообщение от {user_id}: {data}")
            # Здесь будет логика сохранения в БД и отправки другим пользователям или реализую в services

    except WebSocketDisconnect:
        del active_connections[user_id]
        print(f"Пользователь {user_id} отключился")
