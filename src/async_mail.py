import aiohttp,asyncio
class AsyncClient():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://api.internal.temp-mail.io/api/v3"
		self.token=None
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def new_email(self):
		async with self.session.post(f"{self.api}/email/new",headers=self.headers) as req:
			data=await req.json()
			self.token=data['token']
			return data
	async def remove_email(self,email):
		data={"token":self.token}
		async with self.session.delete(f"{self.api}/email/{email}",headers=self.headers,json=data) as req:
			return await req.text()
	async def messages_email(self,email):
		async with self.session.get(f"{self.api}/email/{email}/messages",headers=self.headers) as req:
			return await req.json()