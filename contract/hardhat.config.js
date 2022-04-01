require("@nomiclabs/hardhat-waffle");

// This is a sample Hardhat task. To learn how to create your own go to
// https://hardhat.org/guides/create-task.html
task("accounts", "Prints the list of accounts", async (taskArgs, hre) => {
  const accounts = await hre.ethers.getSigners();

  for (const account of accounts) {
    console.log(account.address);
  }
});

// You need to export an object to set up your config
// Go to https://hardhat.org/config/ to learn more

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.8.4",
  networks: {
    Rinkeby: {
      url: "https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
      accounts: [
        "dabe4273849175d355b126351cf31bd8888c885dbcd0d3f3a039f0a80cc20341",
      ],
    },
    Ropsten: {
      url: "https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
      accounts: [
        "5aefce0a2d473f59578fa7dee6a122d6509af1e0f79fcbee700dfcfeddabe4cc",
      ],
    },
  },
  etherscan: {
    apiKey: "8XIV94EX1NSACM51CZ6DTNSIUEH2Z587U9",
  },
};
