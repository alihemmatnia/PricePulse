import asyncio
import websockets
import json
from colorama import init, Fore, Style

init(autoreset=True)  

async def main():
    coin = input("Enter coin pair (like USDC_USDT): ").strip().upper()
    url = "wss://bc.kifpool.ws/v2/ws"
    payload = {
        "channel": "spot.tickers",
        "event": "subscribe",
        "payload": [coin]
    }

    last_price = None

    async with websockets.connect(url) as ws:
        await ws.send(json.dumps(payload))
        print(f"Subscribed to {coin}...\n")

        while True:
            message = await ws.recv()
            data = json.loads(message)
            
            result = data.get("result")
            if not result:
                continue

            current_price = result.get("price_sell_irt")
            if not current_price:
                continue

            current_price = round(float(current_price))
            formatted_price = f"{current_price:,}"
            
            if last_price is None:
                print(f"{Fore.WHITE}Price: {formatted_price} IRT")
            else:
                if current_price > last_price:
                    print(f"{Fore.GREEN}Price: {formatted_price} IRT 🔺")
                elif current_price < last_price:
                    print(f"{Fore.RED}Price: {formatted_price} IRT 🔻")
                else:
                    print(f"{Fore.YELLOW}Price: {formatted_price} IRT ➡️")

            last_price = current_price

asyncio.run(main())
