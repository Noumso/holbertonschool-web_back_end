import fs from 'fs/promises';

export async function readDatabase(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    const lines = content.trim().split('\n').slice(1); // remove header

    const studentsByField = {};

    for (const line of lines) {
      const [firstname, , , field] = line.split(',');

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstname);
    }

    return studentsByField;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
