export interface Media {
  id: number;
  original_image?: string;
  isLoading?: boolean;
  name: string;
  conversion_type?: string;
  conversion_date: Date;
  converted_image?: string;
}
