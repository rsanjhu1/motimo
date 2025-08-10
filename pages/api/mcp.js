export default function handler(req, res) {
  if (req.method === 'POST') {
    const { command } = req.body;

    if (command === 'validate') {
      // Your phone number here
      return res.status(200).json({ result: '+919876543210' });
    }

    // For any other command
    return res.status(200).json({ result: `Received command: ${command}` });
  } else {
    res.setHeader('Allow', ['POST']);
    return res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
