import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import NFTCard from "./NFTCard";
import TokenList from "./TokenList";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Django backend URL

export default function WalletDashboard() {
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);
  const [tokens, setTokens] = useState([]);
  const [nfts, setNfts] = useState([]);

  const connectWallet = async () => {
    if (window.ethereum) {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);
      setAccount(accounts[0]);
      fetchWalletData(accounts[0]);
    } else {
      alert("MetaMask is required to connect.");
    }
  };

  const fetchWalletData = async (address) => {
    try {
      const balanceRes = await fetch(`${API_BASE_URL}/balance/${address}/`);
      const balanceData = await balanceRes.json();
      setBalance(balanceData.balance);

      const tokenRes = await fetch(`${API_BASE_URL}/tokens/${address}/`);
      const tokenData = await tokenRes.json();
      setTokens(tokenData.tokens || []);

      const nftRes = await fetch(`${API_BASE_URL}/nfts/${address}/`);
      const nftData = await nftRes.json();
      setNfts(nftData.nfts || []);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Ethereum Wallet Dashboard</h1>
      <Button onClick={connectWallet} className="mt-4">
        {account ? `Connected: ${account.slice(0, 6)}...` : "Connect Wallet"}
      </Button>

      {account && (
        <Card className="mt-4">
          <CardContent>
            <p>Address: {account}</p>
            <p>Balance: {balance} ETH</p>
          </CardContent>
        </Card>
      )}

      <TokenList tokens={tokens} />

      <h2 className="mt-4 text-xl font-bold">NFTs</h2>
      <div className="grid grid-cols-2 gap-4">
        {nfts.map((nft, index) => (
          <NFTCard key={index} nft={nft} />
        ))}
      </div>
    </div>
  );
}



