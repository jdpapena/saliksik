import axios from "axios";
import type { StockAnalysis } from "../types/stock";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000",
});

export const getStockAnalysis = async (
  ticker: string,
): Promise<StockAnalysis> => {
  const response = await api.get<StockAnalysis>(
    `/stocks/${ticker}/analysis`,
  );
  return response.data;
};