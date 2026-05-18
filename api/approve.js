module.exports = async (req, res) => {

  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {

    const paymentId = req.body.paymentId;

    const response = await fetch(
      `https://api.minepi.com/v2/payments/${paymentId}/approve`,
      {
        method: "POST",

        headers: {
          "Authorization":
            "Key 6gv2wlgs5ucf99622gbfnmfnsdwqu5cewvdjwd5fcsz2flbp2mf2vpft2afyio1f",
          "Content-Type": "application/json"
        }
      }
    );

    const data = await response.json();

    res.status(200).json({
      success: true,
      data
    });

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.toString()
    });
  }
};
