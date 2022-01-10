import plover  # type: ignore
import time

def comment(engine: 'plover.engine.StenoEngine', argument: str)->None:
	pass

def comment_meta(context: 'plover.formatting._Context', argument: str) -> 'plover.formatting._Action':
	return context.copy_last_action()
