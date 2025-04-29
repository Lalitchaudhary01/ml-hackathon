const express = require("express");
const router = express.Router();
const Student = require("../models/Student");

// Add a new student
router.post("/", async (req, res) => {
  try {
    const student = new Student(req.body);
    await student.save();
    res.json(student);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all students
router.get("/", async (req, res) => {
  try {
    const students = await Student.find();
    res.json(students);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

module.exports = router;
