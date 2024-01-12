### async_mail.py

async library for temp-mail.io

![i-5](https://github.com/aminobotskek/temp_mail/assets/94906343/0eccf6b6-fe82-4374-8585-048453926846)


# Install
```
git clone https://github.com/aminobotskek/async_mail
```

### Example
```python3
import async_mail
import asyncio
async def main():
	client=async_mail.AsyncClient()
	data= await client.new_email()
	print(data)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
