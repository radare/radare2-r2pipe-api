from .base import R2Base

class Print(R2Base):
	def __init__(self, r2):
		super(Print, self).__init__(r2)
		self.hash_types = self._exec('ph').split()

	def byte(self):
		return self.bytes(1)[0]

	def bytes(self, size):
		ret = self._exec('p8j %s%s' % (size, self._tmp_off), json=True)
		self._tmp_off = ''
		return ret

	def disassemble(self, size=0):
		ret = self._exec('pdj %s%s' % ('' if size == 0 else size,
									   self._tmp_off), json=True)
		self._tmp_off = ''
		return ret

	def hash(self, h_type, size=0):
		if h_type not in self.hash_types:
			raise ValueError('Hash function not supported')
		size = '' if size == 0 else size
		ret = self._exec('ph %s %s%s' % (h_type, size, self._tmp_off))
		self._tmp_off = ''
		return ret

	@property
	def pwd(self):
		return self._exec('pwd')
