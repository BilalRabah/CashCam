const axios = require('axios');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const paymentId = req.body.paymentId;

  try {
    await axios.post(
      `https://api.minepi.com/v2/payments/${paymentId}/approve`,
      {},
      {
        headers: {
          Authorization: 'Key 6gv2wlgs5ucf99622gbfnmfnsdwqu5cewvdjwd5fcsz2flbp2mf2vpft2afyio1f'
        }
      }
    );

    res.send({ success: true });
  } catch (error) {
    res.status(500).send({ success: false, error: error.message });
  }
};
