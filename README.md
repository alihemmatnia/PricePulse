# PricePulse

**PricePulse** is a Python program for monitoring live cryptocurrency prices using the **KifPool WebSocket API**. It allows you to:

- Receive real-time updates for a specific crypto pair (e.g., `USDC_USDT`).
- See price changes with arrows and colors (🔺 up – 🔻 down – ➡️ unchanged).
- Display prices with rounded values and comma-separated digits for readability.

## Features

- Easy connection to the KifPool WebSocket
- Color-coded live price updates
- Rounded prices and formatted numbers for clarity
- Can be extended for multiple crypto pairs

## Example Run

```
$ python main.py

Enter coin pair (like USDC_USDT): USDC_USDT

Price: 99,550 IRT 🔺
Price: 99,540 IRT 🔻
Price: 99,540 IRT ➡️
```
