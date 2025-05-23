import { readDatabase } from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const path = process.argv[2];
      const data = await readDatabase(path);
      const fields = Object.keys(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      let output = 'This is the list of our students';

      for (const field of fields) {
        const list = data[field];
        output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }

      res.status(200).send(output);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    const allowed = ['CS', 'SWE'];

    if (!allowed.includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const path = process.argv[2];
      const data = await readDatabase(path);
      const list = data[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
