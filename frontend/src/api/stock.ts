import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getStockAnalysis = async (ticker: string) => {
  const response = await api.get(`/stocks/${ticker}/analysis`);
  return response.data;
};