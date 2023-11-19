class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Invalid worker instance")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  # Use the setter to ensure validation

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss:
                # Remove worker from the previous boss's list
                self._boss.workers.remove(self)
            # Set the new boss and add the worker to the new boss's list
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Invalid boss instance")


# Example usage:
boss1 = Boss(1, "Boss1", "CompanyA")
boss2 = Boss(2, "Boss2", "CompanyB")

worker1 = Worker(101, "Worker1", "CompanyA", boss1)
print(f"Worker1's boss: {worker1.boss.name}")
print(f"Boss1's workers: {[w.name for w in boss1.workers]}")

# Reassigning the boss for worker1
worker1.boss = boss2
print(f"Worker1's new boss: {worker1.boss.name}")
print(f"Boss1's updated workers: {[w.name for w in boss1.workers]}")
print(f"Boss2's workers: {[w.name for w in boss2.workers]}")