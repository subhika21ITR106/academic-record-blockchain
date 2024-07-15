import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.student_id = student_id
        self.course_id = course_id
        self.course_name = course_name
        self.grade = grade
        self.semester = semester
        self.hash = hash
        self.nonce = nonce

class AcademicRecordBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(
            0, "0", int(time.time()), 
            "GenesisStudent", "GenesisCourse", 
            "GenesisCourseName", "GenesisGrade", "GenesisSemester", 
            self.calculate_hash(0, "0", int(time.time()), "GenesisStudent", "GenesisCourse", "GenesisCourseName", "GenesisGrade", "GenesisSemester", 0), 
            0
        )
        self.chain.append(genesis_block)

    def add_academic_record(self, student_id, course_id, course_name, grade, semester):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester, nonce)
        new_block = Block(index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, student_id, course_id, course_name, grade, semester, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(student_id) + str(course_id) + str(course_name) + str(grade) + str(semester) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    academic_record_blockchain = AcademicRecordBlockchain()
    academic_record_blockchain.add_academic_record("Student_1", "Course_1", "Math 101", "A", "Fall 2023")
    academic_record_blockchain.add_academic_record("Student_2", "Course_2", "History 101", "B", "Spring 2024")
    academic_record_blockchain.add_academic_record("Student_3", "Course_3", "Science 101", "A-", "Fall 2024")
    academic_record_blockchain.print_chain()
